<?php
echo 'hola';
$conn=mysqli_connect("localhost","root","","atenea"); 

$usu_usuario=$_POST['Nom'];
$usu_password=$_POST['u_password'];
$sentencia=$conn->prepare("SELECT * FROM estudiants WHERE Nom=? AND u_password=?");
$sentencia->bind_param('ss',$usu_usuario,$usu_password);
$sentencia->execute();
$resultado = $sentencia->get_result();
if ($fila = $resultado->fetch_assoc()) {
         echo json_encode($fila,JSON_UNESCAPED_UNICODE);     
}
$sentencia->close();
$conn->close();
?>
