# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 1:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1412 windows, 36276 settled trades, 424 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 727 | 34.8 | 35.3 | $-462.49 | -6.4% | $537.51 | -1.3 | done | can't tell from luck |
| value_ev10 | 1756 | 39.0 | 39.2 | $-727.69 | -4.1% | $272.31 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 3625 | 50.8 | 50.1 | $-1014.85 | -2.8% | $-14.85 | -1.7 | done | can't tell from luck |
| value_ev5 | 2651 | 40.7 | 41.1 | $-1161.65 | -4.4% | $-161.65 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 3047 | 49.3 | 49.3 | $-1437.28 | -4.7% | $-437.28 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 3047 | 50.7 | 51.0 | $-1583.08 | -5.2% | $-583.08 | -2.9 | done | losing for real |
| trend_filter | 2156 | 48.6 | 50.3 | $-1867.18 | -8.7% | $-867.18 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3625 | 49.2 | 50.2 | $-2209.05 | -6.1% | $-1209.05 | -3.7 | done | losing for real |
| coinflip | 5214 | 50.0 | 50.0 | $-2211.81 | -4.2% | $-1211.81 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 5214 | 50.2 | 51.3 | $-3212.97 | -6.2% | $-2212.97 | -4.6 | done | losing for real |
| always_up | 5214 | 47.9 | 49.3 | $-3614.89 | -6.9% | $-2614.89 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9138 | 48.1 | 48.8 | $-4817.30 |
| ETH | 9828 | 48.1 | 48.0 | $-5101.41 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
