import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'gallery_screen.dart';

class MainScreen extends StatefulWidget {
  const MainScreen({super.key});

  @override
  State<MainScreen> createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {
  final ImagePicker _picker = ImagePicker();

  Future<void> _pickImage() async {
    final XFile? pickedFile =
        await _picker.pickImage(source: ImageSource.gallery);
    if (pickedFile != null && mounted) {
      Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) => GalleryScreen(
            selectedImage: pickedFile,
          ),
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text(
              'Under the sea!',
              style: TextStyle(
                fontFamily: 'Georgia',
                fontSize: 32,
                fontStyle: FontStyle.italic,
              ),
            ),
            const SizedBox(height: 30),
            Image.asset(
              'assets/images/cute-jellyfish.png',
              width: 200,
              height: 200,
            ),
            const SizedBox(height: 30),
            ElevatedButton.icon(
              onPressed: _pickImage,
              icon: const Icon(Icons.photo),
              label: const Text('사진 찾아보기'),
              style: ElevatedButton.styleFrom(
                // ignore: deprecated_member_use
                backgroundColor: Colors.grey.withOpacity(0.3),
                padding: const EdgeInsets.all(16),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(10),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
