# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 9:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1206 windows, 33248 settled trades, 171 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 649 | 34.5 | 35.3 | $-438.79 | -6.8% | $561.21 | -1.3 | done | can't tell from luck |
| value_ev10 | 1589 | 38.6 | 39.2 | $-811.29 | -5.1% | $188.71 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3332 | 50.8 | 50.3 | $-1095.29 | -3.3% | $-95.29 | -1.9 | done | can't tell from luck |
| value_ev5 | 2402 | 40.4 | 41.1 | $-1246.97 | -5.2% | $-246.97 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2786 | 49.4 | 49.4 | $-1325.79 | -4.8% | $-325.79 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2786 | 50.6 | 51.1 | $-1622.88 | -5.8% | $-622.88 | -3.2 | done | losing for real |
| trend_filter | 1963 | 48.6 | 50.4 | $-1710.37 | -8.7% | $-710.37 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 3332 | 49.2 | 50.2 | $-2049.91 | -6.2% | $-1049.91 | -3.6 | done | losing for real |
| coinflip | 4803 | 50.1 | 50.1 | $-2168.95 | -4.5% | $-1168.95 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4803 | 50.2 | 51.4 | $-2946.80 | -6.1% | $-1946.80 | -4.4 | done | losing for real |
| always_up | 4803 | 47.9 | 49.3 | $-3468.99 | -7.2% | $-2468.99 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7664 | 48.1 | 48.9 | $-4286.53 |
| ETH | 8274 | 48.0 | 48.3 | $-5015.27 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
