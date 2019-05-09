/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: Mackan
 *
 * Created on November 23, 2017, 9:55 AM
 */

#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

template<typename T>
struct Node {
    Node(int value): value(value) {}
    int value = 0;
    bool visited = false;
    T distance = 0;
    
};

template<typename T>
struct Edge {
    Edge(Node<T>* to, T cost): to(to), cost(cost) {}
    Node<T>* to;
    T cost = 0;
};

template<typename T>
struct Graph {
    std::multimap<Node<T>*, Edge<T>*> adjList;
    std::vector<Node<T>*> nodeList;
    std::vector<Edge<T>*> adjacentEdges(Node<T>* node) {
        std::vector<Edge<T>*> result;
        auto lower = adjList.lower_bound(node);
        auto upper = adjList.upper_bound(node);
        
        for(auto it = lower; it != upper; it++) {
            result.push_back(it->second);
        }
        return result;
    }
    
    void clean() {
        for (auto e: nodeList) {
            e->visited = false;
        }
    }
    
    void createFromAdjMatrix(std::vector<std::vector<T>> adjMatrix) {
        for (int i = 0; i < adjMatrix.size(); i++) {
            nodeList.push_back(new Node<T>(i + 1));
        }
        for (int i = 0; i < adjMatrix.size(); i++) {
            for (int j = 0; j < adjMatrix[i].size(); j++) {
                if(adjMatrix[i][j] > 0) {
                    Edge<T>* edge = new Edge<T>(nodeList[j], adjMatrix[i][j]);
                    adjList.insert(std::pair<Node<T>*, Edge<T>*>(nodeList[i], edge));
                }
            }
        }
    }
};

template<typename T>
struct CompareDist {
    bool operator()(Node<T>* n1, Node<T>* n2) {
        return (n1->distance < n2->distance);
    }
};

std::vector<std::vector<int>> readGraphFromFile(std::string filePath) {
    std::string line = "";
    //Create a resultvector
    std::vector<std::vector<int>> result;
    //Open the file
    std::ifstream file(filePath);
   
    //Iterate over each line in the file and then read each character delimited by spaces
    while (std::getline(file, line)) {
        std::stringstream ss(line);
        std::string out;
        std::vector<int> tempVector;
        
        while (ss >> out) {
            tempVector.push_back(std::stoi(out));
        } 
        result.push_back(tempVector);
    }
    
    file.close();
    return result;
}

template <typename T>
void DFS(Node<T>* start, Graph<T>& graph) {
    std::stack<Node<T>*> stack;
    stack.push(start);
    while (!stack.empty()) {
        start = stack.top(); 
        stack.pop();
        if (!start->visited) {
            start->visited = true;
            std::cout << start->value << std::endl;
            for (auto edge: graph.adjacentEdges(start)) {
                if (!edge->to->visited) {
                    stack.push(edge->to);
                }
            }
        }
    }
}

template <typename T>
void BFS(Node<T>* start, Graph<T>& graph) {
    std::queue<Node<T>*> queue;
    queue.push(start);
    while (!queue.empty()) {
        start = queue.front();
        queue.pop();
        if (!start->visited) {
            start->visited = true;
            std::cout << start->value << std::endl;
            for (auto edge: graph.adjacentEdges(start)) {
                if (!edge->to->visited) {
                    queue.push(edge->to);
                }
            }
        }
    }
}

template <typename T>
void djikstras(Node<T>* start, Graph<T>& graph) {
    std::priority_queue<Node<T>*, std::vector<Node<T>*>, CompareDist<T>> PQ;
    for (auto node: graph.nodeList)
        node->distance = INT_MAX;
    start->distance = 0;
    start->visited = true;
    PQ.push(start);
    
    while (!PQ.empty()) {
        start = PQ.top();
        PQ.pop();
        start->visited = true;
        for (auto edge: graph.adjacentEdges(start)) {
            if (!edge->to->visited && edge->to->distance > start->distance + edge->cost) {
                edge->to->distance = start->distance + edge->cost;
                PQ.push(edge->to);
            }
        }
    }
    
    for(auto node: graph.nodeList) {
        std::cout << node->value << ": " << node->distance << std::endl;
    }
}

/*
 * 
 */
int main(int argc, char** argv) {
    std::vector<std::vector<int>> result = readGraphFromFile("graph.txt");
    Graph<int> g;
    g.createFromAdjMatrix(result);
    std::cout << "Djikstras" << std::endl;
    djikstras(g.nodeList[0], g);
    g.clean();
    
    std::cout << "BFS" << std::endl;
    BFS(g.nodeList[0], g);
    g.clean();
    
    std::cout << "DFS" << std::endl;
    DFS(g.nodeList[0], g);
    
    return 0;
}

