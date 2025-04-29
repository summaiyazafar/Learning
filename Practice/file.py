# print("hello world!")
# for n in range(8):
    # print("Summaiya")
# for p in range(1,11):
    # print("2*",p,"=",2*p)
# for k in range(10,0,-1):reverse form
    # print("10*",k,"=",2*k)

# i=1 #inverse function
# while i<=10:
#     print("Summaiya")
#     i=i+1
# print(i)

# p=10 #reverse function
# while p>=1:
#     print("bibi")
#     p=p-1
# print(p)

# e=7
# while e>=2:
#     print("Sadiqa")
#     e=e-1
# print(e)

# g=2
# while g<=6:
#     print("Insha")
#     g=g+1
# print(g)




<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Flask App</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-SgOJa3DmI69IUzQ2PVdRZhwQ+dy64/BUtbMJw1MZ8t5HZApcHrRKUc4W0kG879m7" crossorigin="anonymous">
  </head>
  <body>
    <div class="container">
      <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">Flask App</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div class="navbar-nav">
              <a class="nav-link active" aria-current="page" href="/">Home</a>
              <a class="nav-link" href="/">Login</a>
              <a class="nav-link" href="/ ">Register</a>
            </div>
          </div>
        </div>
      </nav>
    </div>
    <div class="container mt-5">
      <div class="card py-3 px-3">
        <h1 class="text-success">Register</h1>      
        <form action="" method="post"> 
        <div class="form-floating mb-3">
         <input type="text" class="form-control" name="username" id="floatingInput" placeholder="name@example.com">
         <label for="floatingInput">User name</label>
       </div>
       <div class="form-floating mb-3">
        <input type="text" class="form-control" name="contact" id="floatingInput" placeholder="name@example.com">
        <label for="floatingInput">user contact</label>
      </div>
      <div class="form-floating mb-3">
        <input type="text" class="form-control" name="password" id="floatingInput" placeholder="name@example.com">
        <label for="floatingInput">Password</label>
      <div class="form-floating mb-3">
      <select class="form-select form-select-lg mb-3" name="role" aria-label="Large select example">
        <option selected>Select User</option>
        <option value="admin">Admin</option>
        <option value="user">User</option>
      </select>
      </div>
      <div class="form-floating mb-3">
         <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
         <label for="floatingPassword">Password</label>
       </div>
       <div class="mb-3 mt-2">
         <button class="btn btn-success">Submit</button>
       </div>
 
       </form></div>

   </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/js/bootstrap.bundle.min.js" integrity="sha384-k6d4wzSIapyDyv1kpU366/PK5hCdSbCRGRCMv+eplOQJWyd1fbcAu9OCUj5zNLiq" crossorigin="anonymous"></script>
  </body>

</html>

