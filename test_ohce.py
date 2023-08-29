import ohce

## sys.argv[0]

def test_simple():
    nombre = "Juan"
    assert ohce.ohce(nombre) == ("¡Buenas noches " + nombre + "!")

