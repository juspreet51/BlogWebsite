(function () {
  
  [...document.querySelectorAll(".control")].forEach((button) => {
    button.addEventListener("click", function () {
      document.querySelector(".active-btn").classList.remove("active-btn");
      this.classList.add("active-btn");
      document.querySelector(".active").classList.remove("active");
      document.getElementById(button.dataset.id).classList.add("active");
    });
  });
  document.querySelector(".theme-btn").addEventListener("click", () => {
    document.body.classList.toggle("light-mode");
  });

})();
const handleTag= (tag) => {
  window.location.href=`/category/${tag}`
};

const searchCat=()=>{
    let query=document.getElementById('query-category').value;
    let allCategory=document.querySelectorAll('[id^=cat-title-]')
    if(query.trim()=="")
    {
      for(var i=0;i<allCategory.length;i++){
        let id=(allCategory[i].id).substring(10);
          document.getElementById(`category-${id}`).style.display=""
      }
      return
    }
    query=query.split(",")
    for(q in query){
      q=q.trim()
    }
    console.log(query);
    console.log(allCategory);
    for(var i=0;i<allCategory.length;i++){
      let id=(allCategory[i].id).substring(10);
      console.log(id);
      if(!query.includes(allCategory[i].innerHTML.trim().toLowerCase())){
        document.getElementById(`category-${id}`).style.display="none"
      }else{
        document.getElementById(`category-${id}`).style.display=""
      }
    }
}
const handleBlog=(id)=>{
  window.location.href=`blog/${id}`
}


