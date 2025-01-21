import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import '../services/jellyfish_ai_service.dart';
import 'result_screen.dart';

class ProcessingScreen extends StatefulWidget {
  final XFile image;

  const ProcessingScreen({super.key, required this.image});

  @override
  State<ProcessingScreen> createState() => _ProcessingScreenState();
}

class _ProcessingScreenState extends State<ProcessingScreen> {
  final _aiService = JellyfishAIService();
  double _progress = 0.0;

  @override
  void initState() {
    super.initState();
    _processImage();
  }

  Future<void> _processImage() async {
    try {
      // 진행 상태 애니메이션 시작
      _startProgressAnimation();

      // AI 분석 실행
      final result = await _aiService.identifyJellyfish(widget.image);

      if (mounted) {
        Navigator.pushReplacement(
          context,
          MaterialPageRoute(
            builder: (context) => ResultScreen(
              image: widget.image,
              result: result,
            ),
          ),
        );
      }
    } catch (e) {
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Error: ${e.toString()}')),
        );
      }
    }
  }

  void _startProgressAnimation() {
    Future.delayed(const Duration(milliseconds: 50), () {
      if (_progress < 1.0 && mounted) {
        setState(() {
          _progress += 0.01;
        });
        _startProgressAnimation();
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text(
              'Processing...',
              style: TextStyle(
                fontFamily: 'Georgia',
                fontSize: 32,
                fontStyle: FontStyle.italic,
              ),
            ),
            const SizedBox(height: 30),
            FutureBuilder<String>(
              future: widget.image.readAsString(),
              builder: (context, snapshot) {
                if (snapshot.hasData) {
                  return Image.network(
                    widget.image.path,
                    height: 300,
                    fit: BoxFit.contain,
                  );
                }
                return const CircularProgressIndicator();
              },
            ),
            const SizedBox(height: 30),
            SizedBox(
              width: 200,
              child: LinearProgressIndicator(
                value: _progress,
                backgroundColor: Colors.grey[800],
                valueColor: const AlwaysStoppedAnimation<Color>(Colors.white),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
