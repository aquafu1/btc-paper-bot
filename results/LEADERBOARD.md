# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 9:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1591 windows, 38604 settled trades, 414 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 813 | 34.6 | 35.1 | $-565.00 | -6.9% | $435.00 | -1.5 | done | can't tell from luck |
| value_ev10 | 1920 | 38.5 | 39.0 | $-979.67 | -5.1% | $20.33 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3811 | 50.9 | 50.0 | $-981.14 | -2.6% | $18.86 | -1.6 | done | can't tell from luck |
| value_ev5 | 2881 | 40.5 | 41.0 | $-1400.38 | -4.9% | $-400.38 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 3192 | 51.0 | 50.9 | $-1488.06 | -4.7% | $-488.06 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3192 | 49.0 | 49.2 | $-1693.81 | -5.3% | $-693.81 | -3.0 | done | losing for real |
| trend_filter | 2268 | 48.5 | 50.4 | $-2004.92 | -8.8% | $-1004.92 | -4.3 | done | losing for real |
| coinflip | 5572 | 50.1 | 49.9 | $-2262.05 | -4.1% | $-1262.05 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 3811 | 49.1 | 50.2 | $-2366.13 | -6.2% | $-1366.13 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 5572 | 50.1 | 51.3 | $-3495.79 | -6.3% | $-2495.79 | -4.8 | done | losing for real |
| always_up | 5572 | 48.2 | 49.1 | $-3550.00 | -6.4% | $-2550.00 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10240 | 48.0 | 48.6 | $-5668.97 |
| ETH | 11054 | 48.0 | 47.7 | $-5533.75 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
