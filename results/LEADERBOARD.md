# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 4:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1139 windows, 31482 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 606 | 34.7 | 35.2 | $-372.50 | -6.1% | $627.50 | -1.1 | done | can't tell from luck |
| value_ev10 | 1476 | 38.1 | 39.2 | $-918.98 | -6.2% | $81.02 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 3167 | 50.9 | 50.4 | $-973.24 | -3.1% | $26.76 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2658 | 49.7 | 49.4 | $-1148.98 | -4.3% | $-148.98 | -2.2 | done | losing for real |
| value_ev5 | 2232 | 40.1 | 41.1 | $-1312.81 | -5.9% | $-312.81 | -2.4 | done | losing for real |
| trend_filter | 1868 | 49.0 | 50.5 | $-1466.13 | -7.8% | $-466.13 | -3.5 | done | losing for real |
| reversal_60m_0.30pct | 2658 | 50.3 | 51.1 | $-1662.53 | -6.3% | $-662.53 | -3.3 | done | losing for real |
| coinflip | 4550 | 50.3 | 50.2 | $-1893.68 | -4.2% | $-893.68 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 3167 | 49.1 | 50.2 | $-1977.65 | -6.2% | $-977.65 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 4550 | 50.2 | 51.4 | $-2814.78 | -6.2% | $-1814.78 | -4.3 | done | losing for real |
| always_up | 4550 | 47.7 | 49.3 | $-3443.09 | -7.6% | $-2443.09 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7217 | 48.3 | 49.0 | $-3740.57 |
| ETH | 7797 | 48.1 | 48.4 | $-4650.81 |
| SOL | 8202 | 48.0 | 48.4 | $-4627.14 |
| XRP | 8266 | 48.1 | 48.3 | $-4965.84 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
