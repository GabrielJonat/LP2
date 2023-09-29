package br.com.fiap.conta;
/**
 * Classe que abstrai uma Conta Bancária
 * @author 0030482311032(Gabriel Jonathan de Matos)
 * @version 1.0
 */
public class Conta {
	/**
	 * Número da Conta
	 */
private int numero;

/**
 * Número da Agência
 */
private int agencia;

/**
 * Saldo da Conta
 */
private double saldo;

public Conta() {
	
}

public Conta(int numero, int agencia, double saldo) {
	this.numero = numero;
	this.agencia = agencia;
	this.saldo = saldo;
}

public void setSaldo(double saldo) {
	this.saldo = saldo;
}

public double getSaldo() {
	return saldo;
}

public void setNumero(int valor) {
	this.numero = valor;
}

public int getNumero() {
	return numero;
}

public void setAgencia(int valor) {
	this.agencia = valor;
}

public int getAgencia() {
	return agencia;
}

/**
 * Deposita um valor ao saldo da conta
 * @param valor Valor a ser depositado
 */
public void depositar(double valor) {
	this.saldo += valor;
}

/**
 * Retira um valor do saldo da conta
 * @param valor Valor a ser retirado
 */
public void sacar(double valor) {
	this.saldo -= valor;
}
}
