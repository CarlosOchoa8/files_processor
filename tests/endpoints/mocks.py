SUCCESS_FILE_CONTENT = b"ID,1234\nNombre,\"Juan Perez\"\nFecha Nacimiento,\"23-04-1990\"\nEmail,juan.perez@gmail.com\nMonto,1500.75"
SUCCESS_RESPONSE_TEXT = '"Records inserted properly."'

BAD_FILE_CONTENT = b"ID,1234\nNombre,\"Juan Perez\"\nInvalidField,\"Some Value\"\nMonto,1500.75"
BAD_RESPONSE_TEXT = '{"message":"There are not valid record to store in database: [\'ID,1234\', \'Nombre,\\"Juan Perez\\\"\', \'InvalidField,\\"Some Value\\\"\', \'Monto,1500.75\']"}'
