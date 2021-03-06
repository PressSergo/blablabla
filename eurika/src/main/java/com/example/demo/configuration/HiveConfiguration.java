//package com.example.demo.configuration;
//
//import org.apache.tomcat.jdbc.pool.DataSource;
//import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.beans.factory.annotation.Qualifier;
//import org.springframework.context.annotation.Bean;
//import org.springframework.context.annotation.Configuration;
//import org.springframework.core.env.Environment;
//import org.springframework.jdbc.core.JdbcTemplate;
//
//@Configuration
//public class HiveConfiguration {
//
//    @Autowired
//    private Environment env;
//
//    @Bean(name = "hiveJdbcDataSource")
//    @Qualifier("hiveJdbcDataSource")
//    public DataSource dataSource() {
//        DataSource dataSource = new DataSource();
//        dataSource.setUrl(env.getProperty("hive.url"));
//        dataSource.setDriverClassName(env.getProperty("hive.driver-class-name"));
//        dataSource.setUsername(env.getProperty("hive.username"));
//        dataSource.setPassword(env.getProperty("hive.password"));
//        return dataSource;
//    }
//
//    @Bean(name = "hiveJdbcTemplate")
//    public JdbcTemplate hiveJdbcTemplate(@Qualifier("hiveJdbcDataSource") DataSource dataSource) {
//        return new JdbcTemplate(dataSource);
//    }
//}