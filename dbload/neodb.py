from py2neo import Graph, Node, Relationship
from dbload.loadData import loadData

class neoDB:
    graph = Graph('http://localhost:7474', username='neo4j', password="m19990124")
    myLoad = ""
    treeName = {}
    blobName = {}
    tree2treeName = {}
    tree2blobName = {}

    def __init__(self, loadIn):
        self.myLoad = loadIn
        print("Initial Database")

    def addCommitNodes(self, commitList):
        for comm in commitList:
            sha = comm['sha']
            complete = 0
            message = comm['commit']['message']
            commit_date = comm['commit']['committer']['date']
            committer_name = comm['commit']['committer']['name']
            author_name = comm['commit']['author']['name']
            cont = "MATCH (c:commit) WHERE c.sha=\"" + sha + "\" return c"
            retCon = self.graph.run(cont)
            if str(retCon) == '(No data)':
                print('add a node')
                commitNode = Node("commit", sha=sha, complete=complete, message=message, \
                                  commit_date=commit_date, committer_name=committer_name, \
                                  author_name=author_name)
                self.graph.create(commitNode)

    def addCommitParents(self, commitList):
        for comm in commitList:
            sha = comm['sha']
            for i in comm['parents']:
                pid = i['sha']
                cont = "MATCH (p:commit)-[r:parent]->(u:commit) WHERE p.sha = \"" + \
                       sha + "\" AND u.sha = \"" + pid + "\" return r"
                result = self.graph.run(cont)
                if str(result) == '(No data)':
                    print('add a parent reletionship----------------------------')
                    cont = "MATCH (p:commit),(u:commit) WHERE p.sha = \"" + \
                           sha + "\" AND u.sha = \""+pid + "\" CREATE (p)-[r:parent]->(u)"
                    self.graph.run(cont)
                else:
                    print("parent exists")
                cont = "MATCH (p:commit)-[r:child]->(u:commit) WHERE p.sha = \"" + \
                       pid + "\" AND u.sha = \"" + sha + "\" return r"
                result = self.graph.run(cont)
                if str(result) == '(No data)':
                    print('add a child relationship-----------------------------')
                    cont = "MATCH (p:commit),(u:commit) WHERE p.sha = \"" + pid + \
                           "\" AND u.sha = \"" + sha + "\" CREATE (p)-[r:child]->(u)"
                    self.graph.run(cont)
                else:
                    print("child rela exists")

    def addT2Tree(self, sha):
        treeC = self.myLoad.readTreeF(sha)
        for pa in treeC['tree']:
            if pa['type'] == "blob":
                blobSha = pa['sha']
                if blobSha not in self.blobName:
                    self.blobName[blobSha] = 1
                    cont = "match (b:blob) where b.sha=\"" + blobSha + \
                           "\" return b"
                    cont = self.graph.run(cont)
                    if str(cont) == "(No data)":
                        print("add a blob")
                        blobC = self.myLoad.readBlobF(blobSha)
                        blobNode = Node("blob", sha=blobSha, content=blobC['content'])
                        self.graph.create(blobNode)
                    else:
                        print("blob exists")
                tree2blobs = sha + blobSha
                if tree2blobs not in self.tree2blobName.keys():
                    self.tree2blobName[tree2blobs] = 1
                    cont = "match (t:tree)-[r:tree2blob]->(b:blob) where t.sha = \"" + \
                        sha + "\" and b.sha = \"" + blobSha + "\" return r"
                    cont = self.graph.run(cont)
                    if str(cont) == "(No data)":
                        print("add a tree2blob")
                        cont = "match (t:tree), (b:blob) where t.sha = \"" \
                               + sha + "\" and b.sha = \"" + pa['sha'] + \
                               "\" CREATE (t)-[r:tree2blob{path:\"" + pa['path'] \
                               + "\"}]->(b)"
                        self.graph.run(cont)
                    else:
                        print("tree2blob relationship exists")
                continue
            treeSha = pa['sha']
            if treeSha not in self.treeName.keys():
                self.treeName[treeSha] = 1
                cont = "match (t:tree) where t.sha = \"" + treeSha + "\" return t"
                cont = self.graph.run(cont)
                if str(cont) == "(No data)":
                    print("add a tree")
                    treeNode = Node("tree", sha=pa['sha'])
                    self.graph.create(treeNode)
                else:
                    print("tree exists")
            tree2trees = sha + treeSha
            if tree2trees not in self.tree2treeName.keys():
                self.tree2treeName[tree2trees] = 1
                cont = "match (t1:tree)-[r:tree2tree]->(t2:tree) where t1.sha = \""\
                       + sha + "\" and t2.sha = \"" + treeSha + "\" return r"
                cont = self.graph.run(cont)
                if str(cont) == "(No data)":
                    print("add a tree2tree relationship")
                    cont = "MATCH (t1:tree),(t2:tree) WHERE t1.sha = \"" + \
                           sha + "\" AND t2.sha = \"" + pa['sha'] + \
                           "\" CREATE (t1)-[r:tree2tree{path:\"" + pa['path'] + \
                           "\"}]->(t2)"
                    self.graph.run(cont)
                else:
                    print("tree2tree exists")
            self.addT2Tree(treeSha)

    def addTree(self, commitList):
        n = 0
        for comm in commitList:
            sha = comm['sha']
            print(sha)
            treeSha = comm['commit']['tree']['sha']
            self.treeName[treeSha] = 1
            cont = "match (t:tree) where t.sha = \"" + treeSha + "\" return t"
            cont = self.graph.run(cont)
            if str(cont) != "(No data)":
                print("Tree has already exits " + treeSha)
            else:
                treeNode = Node("tree", sha=treeSha)
                self.graph.create(treeNode)
                print("create a tree node" + treeSha)
            cont = "match (c:commit)-[r:commit2tree]->(t:tree) where c.sha = \"" + \
                   sha + "\" AND t.sha = \"" + treeSha + "\" return r"
            cont = self.graph.run(cont)
            if str(cont) == "(No data)":
                cont = "match (c:commit),(t:tree) where c.sha = \"" + sha + \
                       "\" and t.sha = \"" + treeSha + \
                       "\" create (c)-[r:commit2tree]->(t)"
                self.graph.run(cont)
                print("add a commit2tree " + treeSha)
            else:
                print("commit2tree has already exi" + treeSha)
            self.addT2Tree(treeSha)
            self.myLoad.loadNow(n)
            print(n)
            n += 1

    def addCommitRoot(self, sha):
        cont = "MATCH (c:commit) where c.sha = \"" + sha + "\" set c.root = 1 return c"
        retCon = self.graph.run(cont)
        if str(retCon) == '(No data)':
            return
        print("add root commit")
        return