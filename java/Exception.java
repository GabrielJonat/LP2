package br.com.fiap.tds;
import java.util.Scanner;
import java.util.InputMismatchException;
public class Exceptions {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String resp = new String();
		do{	
			try {
				System.out.println("Informe o dividendo: ");
				int num1 = sc.nextInt();
				System.out.println("Informe o divisor: ");
				int num2 = sc.nextInt();
				double resultado = (double)num1/num2;
				System.out.println("O resultado da divisão é: "+resultado);
				}
			catch(ArithmeticException e){
				System.err.println("Erro ao dividir!");
				}
			catch(InputMismatchException e){
				System.err.println("Erro na entrada de dados!");
				System.out.println("Deseja continuar?");
				resp = sc.next().toUpperCase();
			}
			catch(Exception e){
				System.err.println("Erro!");
				}
			System.out.println("Deseja continuar?");
			resp = sc.next().toUpperCase();
	      }
		while(resp.equals("S")||resp.equals("SIM"));
		sc.close();
	}
}
