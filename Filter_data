/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   Filter_data.cpp
 * Author: Ryan Kallicharran
 *
 * Created on July 10, 2016, 10:47 PM
 */

#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

void print(vector< vector<string> > &map){
    for(int i= 0; i < map.size();i++){
        for(int j =0; j< map[i].size();j++){
            cout<<map[i][j]<<" ";
        }
        cout<<endl;
    }
}
template<typename T>
bool contains(vector<T> &my_var, T my_variable){
   
    for(auto it = my_var.begin(); it != my_var.end(); it++){
        if(*it == my_variable)
            return true;
    }
    return false;
}

bool in_group(string studentx, string studenty){
    
//    check if the exist in the same semester group
//    :param studentx:
//    :param studenty:
//    :return: true if in the group otherwise false
//    
//    # enroll between Apr - Sep -> fall
//    # enroll Mar -> Summer
//    # enroll between Nov - Feb -> Spring
//    # enroll Octuber -> winter
    vector<string> fall = {"Apr", "May", "Jun", "Jul", "Aug", "Sep"};
    vector<string> spring ={"Nov", "Dec", "Feb", "Jan"};
    string monthy = studenty.substr(0,3);
    string yeary = studenty.substr(4,5);
    
    string monthx = studentx.substr(0,3);
    string yearx = studentx.substr(4,5);

    //simple check
    if( (monthy == monthx) && (yearx == yeary) )
        return true;

    if ((monthx == monthy) &&  !(yearx == yeary))
        return false;

    if (yearx == yeary){
        if (contains(fall,monthx) && contains(fall,monthy))
            return true;
    }else{
        if (contains(spring,monthx) && contains(spring,monthy))
            if ( ((stoi(yeary) % stoi(yearx) == 1) && 
                    !(monthx ==("Jan")) && !(monthx ==("Feb")))
                   || ((stoi(yearx) % stoi(yeary) == 1) && 
                    !(monthx ==("Dec")) && !(monthx ==("Nov"))))
                return true;
    }
    return false;
}
int main()
{
    //read file
    std::ifstream  data("example.csv");
    vector< vector<string> > myMap;
    
    std::string line;
    while(std::getline(data,line))
    {
        std::stringstream  lineStream(line);
        std::string        cell;
        vector<string> line_v;
        int num = 0;
        while(std::getline(lineStream,cell,','))
        {
            // extracting data cell by cell into vector
            line_v.push_back(cell);            
            num ++;
            if(num == 5)
                break;
        }
        myMap.push_back(line_v);
    }
    
    data.close();
    //end reading
    
    vector<int> unique_id_list;
    bool check_p = true;
    string student_seen= "";
    unique_id_list.push_back(0);
    
    //make list of repeated students
    for(int i = 1; i<myMap.size();i++){
        if(!(student_seen == myMap[i][0] || (i == myMap.size()-1))){
            unique_id_list.push_back(i);
        }
       student_seen = myMap[i][0];
    }//end for loop
  
    
    

    int j;
    int x;
    int moves = 1;
    for(int i = 1; i< myMap.size();i++){
        bool reset = false;
        double counter = 0;
        double sum = 0;
        vector<int> index_dict;
        
        //check for student repeated range inroder to change j and x
        if(contains(unique_id_list, i)){
            if((moves+1) == unique_id_list.size()){
                break;
            }
            j = unique_id_list[moves];
            x = unique_id_list[moves+1];
            moves++;
        }
        
        //loop over repeated student
        for(j; j<x;j++){     
            if(in_group(myMap[i][3], myMap[j][3])){
               
                string grade = myMap[j][2];
                double gradeD = stod(grade);
                
                sum = gradeD + sum;
                counter = counter + 1;
                index_dict.push_back(j);
            }
        }
        
        //reset
        if(i < j){
            j = j-x +1;
        }
            
        bool skip = false;
        // skip some iteration for speed up
        if(index_dict[0]-index_dict[index_dict.size()-1] == (index_dict.size() -1))
            i = index_dict[index_dict.size()-1];
    
        //decide where to put the semester gpa
        index_dict.pop_back();
        
        if (!contains(index_dict,i)){
            double avg = sum /counter;
            myMap[i].push_back(to_string(avg));         
        }
    }
  
    //write to a file
    ofstream myfile;
    myfile.open ("output.csv");
    for(int i= 0; i < myMap.size();i++){
        for(int j =0; j< myMap[i].size();j++){
            myfile<<myMap[i][j]<<",";
        }
        myfile<<"\n";
    }
    myfile.close();
    
 }
