#include <stdio.h>
int main(void){
    int idade = 18;
    float salario = 1250.75;
    double porcentagem_desconto = 2.5;
    char genero = 'M';
    float altura = 1.63;
    
    printf("\n Idade: %d", idade);
    printf("\n Salário: %.2f", salario);
    printf("\n Desconto (percentual): %.2f", porcentagem_desconto);
    printf("\n Gênero: %c:", genero);
    printf("\n Altura: %.2f", altura);
    return 0;
};


int nota(void){
struct ficha_aluno
{
char nome[40];
int numero;
float nota;
}; // dfeinição da struct, criou o tipo e não a var

// para criar a variável:
struct ficha_aluno aluno;

printf("\n------ Cadastro de aluno -------------\n\n\n");
printf("Nome do aluno……:");
fgets(aluno.nome, 40, stdin); // – a variavel aluno se refere a struct ficha_aluno e terá 40 caracteres. Esse valor virá do teclado( stdin).
printf("Digite o numero do aluno:");
scanf("%d", &aluno.numero); // – armazena na var aluno.numero um valor inteiro.")
printf("Nota do aluno:");
scanf("%f", &aluno.nota);
printf("Nome……….. %s",aluno.nome);
printf("Numero …………%d\n",aluno.numero);
printf("Nota……….. %.2f \n", aluno.nota);// 2f – duas casas decimais
}


// 