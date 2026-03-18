#include <iostream>
#include <string>

typedef struct {
    std::string nap;
    std::string ebredes;
} Nap;

int main() {
    Nap het[7];

    het[0].nap = "Hetfo";       
    het[0].ebredes = "7:30";
    
    het[1].nap = "Kedd";        
    het[1].ebredes = "7:30";
    
    het[2].nap = "Szerda";      
    het[2].ebredes = "7:30";
    
    het[3].nap = "Csutortok";   
    het[3].ebredes = "7:30";
    
    het[4].nap = "Pentek";      
    het[4].ebredes = "7:30";
    
    het[5].nap = "Szombat";     
    het[5].ebredes = "9:00";
    
    het[6].nap = "Vasarnap";    
    het[6].ebredes = "9:00";

    std::cout << "Heti ebredesi idok:\n\n";
    for (int i = 0; i < 7; i++) std::cout << het[i].nap << ": " << het[i].ebredes << std::endl;
    

    return 0;
}
