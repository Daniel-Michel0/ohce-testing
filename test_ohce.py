import ohce
from unittest.mock import patch
import datetime
import io

def test_noche():
    nombre = "Juan"
    with patch("ohce.datetime") as mock_datetime:
        mock_datetime.datetime.now.return_value.hour = 3
        assert ohce.saludos(nombre) == "¡Buenas noches " + nombre + "!"

def test_mañana():
    nombre = "Carlos"
    with patch("ohce.datetime") as mock_datetime:
        mock_datetime.datetime.now.return_value.hour = 9
        assert ohce.saludos(nombre) == "¡Buenos días " + nombre + "!"

def test_tarde():
    nombre = "Robert"
    with patch("ohce.datetime") as mock_datetime:
        mock_datetime.datetime.now.return_value.hour = 15
        assert ohce.saludos(nombre) == "¡Buenas tardes " + nombre + "!"

def test_voltear():
    input_values = ["palindromo"]
    expected_output = "omordnilap\n"

    with patch("builtins.input", side_effect=input_values), patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
        ohce.voltear(input_values[0])

        output = mock_stdout.getvalue()
        assert output == expected_output

def test_palindromo():
    input_values = ["tacocat"]
    expected_output = "¡Bonita palabra!\n"

    with patch("builtins.input", side_effect=input_values), patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
        ohce.palindromo(input_values[0])

        output = mock_stdout.getvalue()
        assert output == expected_output