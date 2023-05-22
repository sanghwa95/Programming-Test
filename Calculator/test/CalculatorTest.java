package Calculator.test;

import static org.junit.Assert.*;

import org.junit.Test;

import Calculator.Calculator;

public class CalculatorTest {

	@Test
	public void testSum() {
		Calculator calculator = new Calculator();
		assertEquals(30, calculator.sum(10, 20));
	}

}
