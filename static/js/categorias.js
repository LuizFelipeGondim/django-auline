
    function CategoriaAnimal(){
        const categorias = JSON.parse(document.getElementById('categorias').textContent);
        const ids = JSON.parse(document.getElementById('ids').textContent);
        for(let i = 0; i < ids.length; i++){
            if (categorias[ids[i]] == 'E'){
                document.getElementById(ids[i]).style.background="green";
            } else if (categorias[ids[i]] == 'P'){
                document.getElementById(ids[i]).style.background="red";
            } else if (categorias[ids[i]] == 'PA'){
                document.getElementById(ids[i]).style.background="blue";
            }
        }
        
    }

    CategoriaAnimal();