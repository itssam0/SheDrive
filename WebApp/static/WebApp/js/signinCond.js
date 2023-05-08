function mostrarContrasena(){
	var tipo = document.getElementById("password");
	var types = document.getElementById("contrasena");
	if(tipo.type == "password"){
		tipo.type = "text";
	}else{
		tipo.type = "password";
	}
	if(types.type == "password"){
		types.type = "text";
	}else{
		types.type = "password";
	}
}