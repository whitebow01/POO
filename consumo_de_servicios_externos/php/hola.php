<!DOCTYPE HTML>
<html>
    <head>
        <title>Prueba de PHP</title>
    </head>
    <body>
        <?php
        echo "<p>Hola Mundo</p>";
        ?>
        <?php
        echo "<p>Cálculo de IVA</p>\n";
        $monto=20000;
        echo "<p>Monto inicial=".$monto."</p>\n";
        $montoFinal=$monto*1.19;
        echo "Total con IVA=".$montoFinal
        ?>
    </body>
</html>