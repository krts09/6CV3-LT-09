<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $boleta = $_POST['boleta'];
    $titulo = $_POST['titulo'];
    $descripcion = $_POST['descripcion'];
    $profesores = $_POST['profesores'];

    // Manejo de la subida del archivo
    $target_dir = "TESCOM_MAIN/trabajos_terminales/";
    $target_file = $target_dir . basename($_FILES["protocolo"]["name"]);
    $uploadOk = 1;
    $fileType = strtolower(pathinfo($target_file, PATHINFO_EXTENSION));

    // Verifica si el archivo ya existe
    if (file_exists($target_file)) {
        echo "El archivo ya existe.";
        $uploadOk = 0;
    }

    // Verifica el tamaño del archivo
    if ($_FILES["protocolo"]["size"] > 500000) {
        echo "El archivo es demasiado grande.";
        $uploadOk = 0;
    }

    // Permite solo ciertos formatos de archivo
    if ($fileType != "pdf" && $fileType != "doc" && $fileType != "docx") {
        echo "Solo se permiten archivos PDF, DOC, y DOCX.";
        $uploadOk = 0;
    }

    // Verifica si $uploadOk es 0 debido a un error
    if ($uploadOk == 0) {
        echo "El archivo no se subió.";
    } else {
        if (move_uploaded_file($_FILES["protocolo"]["tmp_name"], $target_file)) {
            echo "El archivo ". htmlspecialchars(basename($_FILES["protocolo"]["name"])) . " ha sido subido.";

            // Aquí se debe incluir la lógica para insertar los datos en la base de datos
            // Ejemplo de conexión a la base de datos y ejecución de la consulta
            $conn = new mysqli('localhost', 'usuario', 'contraseña', 'base_de_datos');

            if ($conn->connect_error) {
                die("Conexión fallida: " . $conn->connect_error);
            }

            $sql = "INSERT INTO TrabajoTerminal (alumno_id, titulo, descripcion, archivo) VALUES ('$boleta', '$titulo', '$descripcion', '$target_file')";

            if ($conn->query($sql) === TRUE) {
                echo "Nuevo registro creado exitosamente";
            } else {
                echo "Error: " . $sql . "<br>" . $conn->error;
            }

            $conn->close();
        } else {
            echo "Hubo un error al subir el archivo.";
        }
    }
}
?>
