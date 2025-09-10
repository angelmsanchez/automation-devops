
import pytest
from main import saludar

def test_saludar_nombre():
	assert saludar("Mundo") == "¡Hola, Mundo!"

def test_saludar_otro_nombre():
	assert saludar("Ana") == "¡Hola, Ana!"

def test_saludar_vacio():
	assert saludar("") == "¡Hola, !"
