
#include <bits/stdc++.h> 
using namespace std; 

struct Node { 
	int key; 
	struct Node *left, *right; 
}; 

int input(){
	int a;
	cin>>a;
	return a;
}

Node* newNode(int item) 
{ 
	Node* temp = new Node; 
	temp->key = item; 
	temp->left = temp->right = NULL; 
	return temp; 
} 

void inorder(Node* root) 
{ 
	if (root != NULL) { 
		inorder(root->left); 
		printf("%d ", root->key); 
		inorder(root->right); 
	} 
} 

Node* insert(Node* node, int key) 
{ 
	/* If the tree is empty, return a new node */
	if (node == NULL) 
		return newNode(key); 

	/* Otherwise, recur down the tree */
	if (key < node->key) 
		node->left = insert(node->left, key); 
	else
		node->right = insert(node->right, key); 

	/* return the (unchanged) node pointer */
	return node; 
} 

Node* deleteNode(Node* root, int k) 
{ 
	// Base case 
	if (root == NULL) 
		return root; 

	// Recursive calls for ancestors of 
	// node to be deleted 
	if (root->key > k) { 
		root->left = deleteNode(root->left, k); 
		return root; 
	} 
	else if (root->key < k) { 
		root->right = deleteNode(root->right, k); 
		return root; 
	} 

	// We reach here when root is the node 
	// to be deleted. 

	// If one of the children is empty 
	if (root->left == NULL) { 
		Node* temp = root->right; 
		delete root; 
		return temp; 
	} 
	else if (root->right == NULL) { 
		Node* temp = root->left; 
		delete root; 
		return temp; 
	} 

	// If both children exist 
	else { 

		Node* succParent = root; 
		
		// Find successor 
		Node *succ = root->right; 
		while (succ->left != NULL) { 
			succParent = succ; 
			succ = succ->left; 
		} 

		// Delete successor. Since successor 
		// is always left child of its parent 
		// we can safely make successor's right 
		// right child as left of its parent. 
		// If there is no succ, then assign 
		// succ->right to succParent->right 
		if (succParent != root) 
			succParent->left = succ->right; 
		else
			succParent->right = succ->right; 

		// Copy Successor Data to root 
		root->key = succ->key; 

		// Delete Successor and return root 
		delete succ;		 
		return root; 
	} 
} 

bool contains(struct Node* node, int key) 
{ 
    if (node == NULL) 
        return false; 
  
    if (node->key == key) 
        return true; 
  
    /* then recur on left sutree */
    bool res1 = contains(node->left, key); 
  
    if(res1) return true; // node found, no need to look further 
  
    /* node is not found in left, so recur on right subtree */
    bool res2 = contains(node->right, key); 
  
    return res2; 
} 

int size(Node* node)  
{  
    if (node == NULL)  
        return 0;  
    else
        return(size(node->left) + 1 + size(node->right));  
}  

void inorderSuccessor(Node* root, Node* target_node, Node* &next) 
{ 
    // if root is null then return 
    if(!root) 
        return; 
  
    inorderSuccessor(root->right, target_node, next); 
      
    // if target node found then enter this condition 
    if(root->key == target_node->key) 
    { 
        // this will be true to the last node 
        // in inorder traversal i.e., rightmost node. 
        if(next == NULL) 
            cout << "inorder successor of " 
                 << root->key << " is: null\n"; 
        else
            cout << "inorder successor of " 
                 << root->key << " is: " 
                 << next->key << "\n";  
    } 
    next = root; 
    inorderSuccessor(root->left, target_node, next); 
} 

void print(Node* root, string& str) 


{ 
    // bases case 
    if (root == NULL) 
        return; 
  
    // push the root data as character 
	
	str.append(to_string(root->key));
  
    // if leaf node, then return 
    if (!root->left && !root->right) 
        return; 
  
    // for left subtree 
    str.push_back('('); 
    print(root->left, str); 
    str.push_back(')'); 
  
    // only if right child is present to  
    // avoid extra parenthesis 
    if (root->right) { 
        str.push_back('('); 
        print(root->right, str); 
        str.push_back(')'); 
    } 
} 

Node* insertordelete(Node* root, int a){

	 if(!contains(root, a)){
		 root = insert(root, a);
		cout<<"\nValue Inserted"<<endl;
	 }
	 else
	 {
		 root = deleteNode(root, a);
		 cout<<"\nValue Deleted"<<endl;
	 }
	 return root;
}

int main() 
{ 
	
	Node* root = NULL; 
	int choice=0;
	while(true){
		cout<<"\nEnter your choice\n";
		cout<<"1. Insert Or Delete"<<endl
			<<"2. Search"<<endl
			<<"3. Size"<<endl
			<<"4. Next key"<<endl
			<<"5. Print Tree in Bracketed form"<<endl
			<<"6. Exit"<<endl;
		cin>>choice;
			if(choice==1){
				cout<<"\nEnter Value to insert or delete\n";
				root = insertordelete(root, input());
			}
			else if(choice==2){
				cout<<"\nEnter Value to Search\n";
				if(contains(root, input())) cout<<"Tree Contains this value\n";
				else cout<<"Tree doesn't Contains this value\n";
			}
			else if(choice==3){
				cout << "\nSize of the tree is " << size(root)<<endl;  
			}
			else if(choice==4){
				cout<<"\nFind Successor of : \n";
				Node* target;
				Node* next = NULL;
				target->key = input();
    			inorderSuccessor(root, target, next);
			}
			else if(choice==5){
				string str = ""; 
    			print(root, str); 
    			cout <<endl<< str<<endl;
			}
			else if(choice==6){
				return 0;
			}
			else cout<<endl <<"Invalid Input"<<endl;
	}
    return 0;  
} 
