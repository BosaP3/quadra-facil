CREATE TABLE usuarios 
( 
 id_usuario INT PRIMARY KEY DEFAULT 'AUTO_INCREMENT',  
 nome VARCHAR(n) NOT NULL,  
 email VARCHAR(n) NOT NULL,  
 senha VARCHAR(n) NOT NULL,  
 criado_em DATE,  
 tipo_usuario VARCHAR(n) NOT NULL DEFAULT 'ENUM('admin','cliente','dono')',  
); 

CREATE TABLE espacos 
( 
 id_espaco INT PRIMARY KEY AUTO_INCREMENT,  
 id_usuario INT,  
 nome VARCHAR(n) NOT NULL,  
 endereco VARCHAR(n),  
 valor_hora FLOAT NOT NULL,  
 criado_em DATE,  
); 

CREATE TABLE agendamentos 
( 
 id_agendamento INT PRIMARY KEY AUTO_INCREMENT,  
 id_usuario INT,  
 data_hora DATE NOT NULL,  
 status INT NOT NULL DEFAULT 'ENUM('pendente','confirmado','cancelado')',  
 criado_em DATE,  
 id_espaco INT,  
 CHECK (status BETWEEN pendente AND confirmado)
); 

CREATE TABLE partidas 
( 
 id_partida INT PRIMARY KEY AUTO_INCREMENT,  
 id_agendamento INT,  
 descricao VARCHAR(n),  
 regras VARCHAR(n),  
); 

CREATE TABLE participantes_partida 
( 
 id_partida INT,  
 id_usuario INT,  
 papel VARCHAR(n) DEFAULT 'ENUM('organizador','jogador','convidado')',  
); 

ALTER TABLE espacos ADD FOREIGN KEY(id_usuario) REFERENCES usuarios (id_usuario)
ALTER TABLE agendamentos ADD FOREIGN KEY(id_usuario) REFERENCES usuarios (id_usuario)
ALTER TABLE agendamentos ADD FOREIGN KEY(id_espaco) REFERENCES espacos (id_espaco)
ALTER TABLE partidas ADD FOREIGN KEY(id_agendamento) REFERENCES agendamentos (id_agendamento)
ALTER TABLE participantes_partida ADD FOREIGN KEY(id_partida) REFERENCES partidas (id_partida)
ALTER TABLE participantes_partida ADD FOREIGN KEY(id_usuario) REFERENCES usuarios (id_usuario)
