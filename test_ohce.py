import ohce
from unittest.mock import patch
import datetime

def test_noche():
    nombre = "Juan"
    with patch("ohce.datetime") as mock_datetime:
        mock_datetime.datetime.now.return_value.hour = 3
        assert ohce.ohce(nombre) == "¡Buenas noches " + nombre + "!"

def test_mañana():
    nombre = "Carlos"
    with patch("ohce.datetime") as mock_datetime:
        mock_datetime.datetime.now.return_value.hour = 9
        assert ohce.ohce(nombre) == "¡Buenos días " + nombre + "!"

def test_tarde():
    nombre = "Robert"
    with patch("ohce.datetime") as mock_datetime:
        mock_datetime.datetime.now.return_value.hour = 15
        assert ohce.ohce(nombre) == "¡Buenas tardes " + nombre + "!"
