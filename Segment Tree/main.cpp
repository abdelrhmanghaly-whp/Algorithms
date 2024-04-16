#include<bits/stdc++.h>

struct Node{
    long long val;
    Node(){
        val=1e5;
    }
    Node(long long n){
        val=n;
    }
};

struct SegmentTree{
    int size;
    std::vector<Node>data;
    SegmentTree(int n){
        size=1;
        while(size<n)size*=2;
        data.resize(2*size,Node());
    }
    Node merge(Node& l, Node&r){
        Node res=Node();
        res.val=std::min(l.val,r.val);
        return res;
    }
    void build(std::vector<long long>&v, int ni, int lx, int rx){
        int sz=v.size();
        if(rx-lx==1){
            if(lx<sz)data[ni]=Node(v[lx]);
            return;
        }
        int mid=lx+(rx-lx)/2;
        build(v,2*ni+1,lx,mid);
        build(v,2*ni+2,mid,rx);
        data[ni]=merge(data[2*ni+1],data[2*ni+2]);
    }
    void build(std::vector<long long> &v){
        build(v,0,0,size);
    }
    void set(int idx, long long value, int node, int lx, int rx){
        if(rx-lx==1){
            data[node]=Node(value);
            return;
        }
        int mid=lx+(rx-lx)/2;
        if(idx<mid)set(idx,value,2*node+1,lx,mid);
        else set(idx,value,2*node+2,mid,rx);
        data[node]=merge(data[2*node+1],data[2*node+2]);
    }
    void set(int idx, long long value){
        set(idx,value,0,0,size);
    }

    Node getRange(int l,int r, int node, int lx, int rx){
        if(lx>=l && rx<=r)return data[node];
        if(rx<=l || lx>=r)return Node();
        int mid=lx+(rx-lx)/2;
        Node left=getRange(l,r,2*node+1,lx,mid);
        Node right=getRange(l,r,2*node+2,mid,rx);
        return merge(left,right);
    }
    long long getRange(int l, int r){
        return getRange(l,r,0,0,size).val;
    }
//    void print(int node, int level) {
//        if (node>=size) {
//            std::cout<<std::string(level, '\t')<<"Leaf Node: "<<data[node].val <<std::endl;
//            return;
//        }
//        print(2*node+2,level+1);
//        std::cout<<std::string(level, '\t')<<"Internal Node: "<<data[node].val<<std::endl;
//        print(2*node+1,level+1);
//    }
//
//    void print() {
//        print(0, 0);
//    }
};
int main(){
    std::vector<long long>v={1,3,2,7,9,11};
    SegmentTree Seg(v.size());
    Seg.build(v);
    //Seg.print();
    std::cout<<' ------- ';
    std::cout<<"min val in range 1 to 4 "<<Seg.getRange(1,4)<<std::endl;
    Seg.set(2,5);
    std::cout<<"min val in range 1 to 4 after update "<<Seg.getRange(1,4)<<std::endl;
}