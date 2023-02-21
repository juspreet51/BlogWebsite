(function () {
  
  [...document.querySelectorAll(".control")].forEach((button) => {
    button.addEventListener("click", function () {
      document.querySelector(".active-btn").classList.remove("active-btn");
      this.classList.add("active-btn");
      // document.querySelector(".active").classList.remove("active");
      console.log(button.dataset.id);
      // document.getElementById(button.dataset.id).focus();
      
    });
  });
  document.querySelector(".theme-btn").addEventListener("click", () => {
    document.body.classList.toggle("light-mode");
  });
  document.querySelector(".theme-btn1").addEventListener("click", () => {
    if(history.back()===undefined){
      window.location.href='/'
    }
    history.back();
  });

})();
const handleTag= (tag) => {
  // window.location.href=`/category/${tag}`
  window.open(`/category/${tag}`, '_blank');
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
    const lowercaseWords = [];
    query.forEach(word => lowercaseWords.push(word.toLowerCase()));
    console.log(query);
    console.log(allCategory);
    for(var i=0;i<allCategory.length;i++){
      let id=(allCategory[i].id).substring(10);
      console.log(id);
      if(!lowercaseWords.includes(allCategory[i].innerHTML.toLowerCase().trim())){
        document.getElementById(`category-${id}`).style.display="none"
      }else{
        document.getElementById(`category-${id}`).style.display=""
      }
    }
}
const handleBlog=(title)=>{
  console.log(title);
  // window.location.href=`blog/${id}`
  window.open(
    `blog/${title}`,
    '_blank' 
  );
}

