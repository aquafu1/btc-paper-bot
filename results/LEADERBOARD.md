# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 9:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1588 windows, 38573 settled trades, 389 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 813 | 34.6 | 35.1 | $-565.00 | -6.9% | $435.00 | -1.5 | done | can't tell from luck |
| value_ev10 | 1920 | 38.5 | 39.0 | $-979.67 | -5.1% | $20.33 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3807 | 50.9 | 50.0 | $-988.10 | -2.6% | $11.90 | -1.6 | done | can't tell from luck |
| value_ev5 | 2880 | 40.5 | 41.0 | $-1415.24 | -4.9% | $-415.24 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 3188 | 50.9 | 50.9 | $-1517.76 | -4.8% | $-517.76 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3188 | 49.1 | 49.2 | $-1653.81 | -5.2% | $-653.81 | -2.9 | done | losing for real |
| trend_filter | 2266 | 48.5 | 50.3 | $-1984.92 | -8.8% | $-984.92 | -4.3 | done | losing for real |
| coinflip | 5568 | 50.1 | 49.9 | $-2279.87 | -4.1% | $-1279.87 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3807 | 49.1 | 50.2 | $-2348.87 | -6.2% | $-1348.87 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5568 | 50.1 | 51.3 | $-3478.53 | -6.2% | $-2478.53 | -4.8 | done | losing for real |
| always_up | 5568 | 48.2 | 49.1 | $-3579.70 | -6.4% | $-2579.70 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10224 | 48.0 | 48.6 | $-5680.78 |
| ETH | 11039 | 48.0 | 47.7 | $-5526.45 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
