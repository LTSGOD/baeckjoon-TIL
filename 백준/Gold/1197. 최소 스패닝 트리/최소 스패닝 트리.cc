#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge {
    int u, v, weight;
    bool operator<(const Edge& other) const {
        return weight < other.weight;
    }
};

vector<int> parent, rankArr;

// Find the root of the set containing x
int find(int x) {
    if (parent[x] != x) {
        parent[x] = find(parent[x]); // Path compression
    }
    return parent[x];
}


bool unionSets(int x, int y) {
    x = find(x);
    y = find(y);
    if (x == y) return false; // Already in the same set
    
    if (rankArr[x] < rankArr[y]) swap(x, y);
    parent[y] = x;
    if (rankArr[x] == rankArr[y]) rankArr[x]++;
    return true;
}

int main() {
    int V, E;
    cin >> V >> E;

    vector<Edge> edges(E);

    for (int i = 0; i < E; i++) {
        cin >> edges[i].u >> edges[i].v >> edges[i].weight;
    }


    sort(edges.begin(), edges.end());


    parent.resize(V + 1);
    rankArr.resize(V + 1, 0);
    for (int i = 1; i <= V; i++) {
        parent[i] = i;
    }

    long long mstWeight = 0;
    int edgeCount = 0;

    for (const auto& edge : edges) {
        if (unionSets(edge.u, edge.v)) {
            mstWeight += edge.weight;
            edgeCount++;
            if (edgeCount == V - 1) break; 
        }
    }

    cout << mstWeight << endl;

    return 0;
}
