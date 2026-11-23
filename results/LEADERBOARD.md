# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 3:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1182 windows, 32669 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 638 | 35.0 | 35.3 | $-353.40 | -5.5% | $646.60 | -1.1 | done | can't tell from luck |
| value_ev10 | 1550 | 38.6 | 39.2 | $-765.47 | -4.9% | $234.53 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3273 | 50.7 | 50.3 | $-1104.39 | -3.4% | $-104.39 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2750 | 49.7 | 49.4 | $-1183.92 | -4.3% | $-183.92 | -2.3 | done | losing for real |
| value_ev5 | 2344 | 40.3 | 41.1 | $-1242.56 | -5.3% | $-242.56 | -2.2 | done | losing for real |
| trend_filter | 1931 | 48.9 | 50.5 | $-1564.65 | -8.1% | $-564.65 | -3.6 | done | losing for real |
| reversal_60m_0.30pct | 2750 | 50.3 | 51.0 | $-1712.32 | -6.2% | $-712.32 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 3273 | 49.3 | 50.2 | $-1949.85 | -6.0% | $-949.85 | -3.4 | done | losing for real |
| coinflip | 4720 | 50.0 | 50.1 | $-2148.49 | -4.6% | $-1148.49 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4720 | 50.1 | 51.4 | $-2976.20 | -6.3% | $-1976.20 | -4.5 | done | losing for real |
| always_up | 4720 | 47.9 | 49.3 | $-3355.46 | -7.1% | $-2355.46 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7493 | 48.2 | 48.9 | $-4061.74 |
| ETH | 8101 | 48.1 | 48.4 | $-4817.66 |
| SOL | 8497 | 48.2 | 48.4 | $-4432.69 |
| XRP | 8578 | 48.1 | 48.2 | $-5044.61 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
