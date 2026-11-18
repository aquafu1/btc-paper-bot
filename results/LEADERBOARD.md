# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 5:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 711 windows, 19600 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 373 | 34.0 | 34.9 | $-254.03 | -6.8% | $745.97 | -1.0 | done | can't tell from luck |
| value_ev10 | 903 | 38.3 | 39.1 | $-522.57 | -5.8% | $477.43 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 2010 | 51.6 | 50.8 | $-523.12 | -2.6% | $476.88 | -1.2 | done | can't tell from luck |
| momentum_60m_0.30pct | 1648 | 50.2 | 49.5 | $-523.19 | -3.2% | $476.81 | -1.3 | done | can't tell from luck |
| value_ev5 | 1359 | 40.8 | 41.1 | $-602.22 | -4.4% | $397.78 | -1.4 | done | can't tell from luck |
| trend_filter | 1141 | 50.3 | 50.9 | $-627.95 | -5.5% | $372.05 | -1.9 | done | can't tell from luck |
| coinflip | 2836 | 50.2 | 50.3 | $-1192.33 | -4.2% | $-192.33 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1648 | 49.8 | 51.3 | $-1246.22 | -7.6% | $-246.22 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 2836 | 51.1 | 51.8 | $-1402.69 | -4.9% | $-402.69 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2010 | 48.4 | 50.0 | $-1418.15 | -7.1% | $-418.15 | -3.2 | done | losing for real |
| always_up | 2836 | 47.3 | 49.6 | $-2425.26 | -8.6% | $-1425.26 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4444 | 48.2 | 49.1 | $-2645.40 |
| ETH | 4876 | 48.4 | 48.5 | $-2723.84 |
| SOL | 5114 | 48.2 | 48.7 | $-2874.59 |
| XRP | 5166 | 48.6 | 48.4 | $-2493.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
