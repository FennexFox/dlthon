import 'package:flutter/material.dart';
import 'screens/main_screen.dart';

void main() {
  runApp(const JellyfishIdentifierApp());
}

class JellyfishIdentifierApp extends StatelessWidget {
  const JellyfishIdentifierApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Jellyfish Identifier',
      theme: ThemeData.dark().copyWith(
        scaffoldBackgroundColor: Colors.black,
      ),
      home: const MainScreen(),
    );
  }
}
