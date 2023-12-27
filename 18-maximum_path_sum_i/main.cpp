#include <stdio.h>
#include <stdlib.h>

// I create a structure for having the given data as a graph

typedef struct nodo
{
    int vllegada;
    int dist;
    nodo *izq;
    nodo *der;
}nodo;

// Given the data, this function recursivly creates the corresponding graph

nodo* armar_grafo(int* numeros, int indice, int cant_nivel, int max)
{
    if (indice < max)
    {
        nodo *ABb = new nodo;
        ABb->vllegada = numeros[indice];
        ABb->dist = -1;
        ABb->izq = armar_grafo(numeros, indice + cant_nivel, cant_nivel + 1, max);
        ABb->der = armar_grafo(numeros, indice + cant_nivel + 1, cant_nivel + 1, max);
        return ABb;
    }
    return NULL;
}

// A modified version of the dijkstras Algorith to find the maximum path in the graph from the top to every node, except that the first node insted of having distance 0 has distance numeros[0]
// Also wile we calculate the distances we also determine the maximum one
// (This is a simplified version of the algorith just for the sake of the problem, since it is somehow similar to a tree, we will treat it as such, since it won't affect that much efficiency)
void dijkstras(nodo *Abb, int dist_padre, int *max)
{
    if ( Abb != NULL )
    {
        if ( Abb->dist < (dist_padre + Abb->vllegada) ) Abb->dist = dist_padre + Abb->vllegada;
        if (Abb->dist > *max)
            *max = Abb->dist;
        dijkstras(Abb->izq, Abb->dist, max);
        dijkstras(Abb->der, Abb->dist, max);
    }
}

int main()
{

    int numeros[] = {75 , 95 , 64 , 17 , 47 , 82 , 18 , 35 , 87 , 10 , 20 , 4 , 82 , 47 , 65 , 19 , 1 , 23 , 75 , 3 , 34 , 88 , 2 , 77 , 73 , 7 , 63 , 67 , 99 , 65 , 4 , 28 , 6 , 16 , 70 , 92 , 41 , 41 , 26 , 56 , 83 , 40 , 80 , 70 , 33 , 41 , 48 , 72 , 33 , 47 , 32 , 37 , 16 , 94 , 29 , 53 , 71 , 44 , 65 , 25 , 43 , 91 , 52 , 97 , 51 , 14 , 70 , 11 , 33 , 28 , 77 , 73 , 17 , 78 , 39 , 68 , 17 , 57 , 91 , 71 , 52 , 38 , 17 , 14 , 91 , 43 , 58 , 50 , 27 , 29 , 48 , 63 , 66 , 4 , 68 , 89 , 53 , 67 , 30 , 73 , 16 , 69 , 87 , 40 , 31 , 4 , 62 , 98 ,27 ,23 ,9 , 70 , 98 , 73 , 93 , 38 , 53 , 60 , 4 , 23 };
    //int numeros[] = {3, 7, 4, 2, 4, 6, 8, 5, 9, 3 };    
    nodo *ABB = armar_grafo(numeros, 0, 1, sizeof(numeros)/4);
    ABB->dist = numeros[0];
    int *max = new int;
    dijkstras(ABB, 0, max);
    printf("La distancia maxima encontrada fue %d .\n", *max);

    return 0;
}