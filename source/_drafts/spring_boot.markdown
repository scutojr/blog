---
title: spring boot usage
categories: []
---

# Sprint Boot


**List of Spring Boot Annotation**
- @RequestMapping, @GetMapping, @PostMapping
- @RestController, @Controller
- @Configuration
- @EnableAutoConfiguration  # You should only ever add one @EnableAutoConfiguration annotation.
- [@SpringBootApplication](https://docs.spring.io/spring-boot/docs/current/reference/html/using-boot-using-springbootapplication-annotation.html)
```
The @SpringBootApplication annotation is equivalent to using @Configuration, @EnableAutoConfiguration and @ComponentScan with their default attributes:
```
- @ComponentScan (to find your beans)
- @Autowired (to do constructor injection)
- @Component
- @Value
- @RestController = @Controller + @ResponseBody
- @ResponseBody annotation tells Spring MVC not to render a model into a view
- @RequestBody, used in parameter, support POJO rule


spring中component指的是哪些？
```
All of your application components (@Component, @Service, @Repository, @Controller.) are automatically registered as Spring Beans.

@Bean 应该也是
```

@Configuration怎么用？

Many Spring Boot developers always have their main class annotated with @Configuration, @EnableAutoConfiguration, and @ComponentScan. Since these annotations are so frequently used together (especially if you follow the best practices above), Spring Boot provides a convenient @SpringBootApplication alternative.


@SpringBootApplication = @Configuration +@EnableAutoConfiguration + @ComponentScan

```
package com.example.myapplication;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication // same as @Configuration @EnableAutoConfiguration @ComponentScan
public class Application {

  public static void main(String[] args) {
    SpringApplication.run(Application.class, args);
  }

}
```

# TODO

1. a relation hierarchy of annotation is necessary?
