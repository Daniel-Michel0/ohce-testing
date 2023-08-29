import ohce
from unittest.mock import patch
import datetime
## sys.argv[0]

def test_noche():
    nombre = "Juan"
    with patch("ohce.datetime") as mock_datetime:
        mock_datetime.datatime.now.return_value.hour = 3
        assert ohce.ohce(nombre) == "¡Buenas noches " + nombre + "!"

def test_mañana():
    nombre = "Juan"
    with patch("ohce.datetime") as mock_datetime:
        mock_datetime.datatime.now.return_value.hour = 9
        assert ohce.ohce(nombre) == "¡Buenos días " + nombre + "!"

def test_tarde():
    nombre = "Juan"
    with patch("ohce.datetime") as mock_datetime:
        mock_datetime.datatime.now.return_value.hour = 15
        assert ohce.ohce(nombre) == "¡Buenas tardes " + nombre + "!"
