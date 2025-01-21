import 'package:image_picker/image_picker.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;

class JellyfishResult {
  final String species;
  final String description;
  final double confidence;

  JellyfishResult({
    required this.species,
    required this.description,
    required this.confidence,
  });

  factory JellyfishResult.fromJson(Map<String, dynamic> json) {
    return JellyfishResult(
      species: json['species'],
      description: json['description'],
      confidence: json['confidence'].toDouble(),
    );
  }
}

class JellyfishAIService {
  static const String apiUrl = 'YOUR_AI_API_ENDPOINT'; // AI 서비스 엔드포인트로 변경 필요

  Future<JellyfishResult> identifyJellyfish(XFile image) async {
    try {
      final bytes = await image.readAsBytes();
      final base64Image = base64Encode(bytes);

      final response = await http.post(
        Uri.parse(apiUrl),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({
          'image': base64Image,
        }),
      );

      if (response.statusCode == 200) {
        final result = JellyfishResult.fromJson(jsonDecode(response.body));
        return result;
      } else {
        throw Exception('Failed to identify jellyfish');
      }
    } catch (e) {
      // 테스트용 더미 데이터 반환
      return JellyfishResult(
        species: "Lion's Mane Jellyfish",
        description:
            "The Lion's Mane Jellyfish (Cyanea capillata) is one of the largest jellyfish species, known for its massive bell, long tentacles that can reach up to 30 meters, and its ability to sting with venom to capture prey in cold northern ocean waters.",
        confidence: 0.95,
      );
    }
  }
}
