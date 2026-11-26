# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 5:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1525 windows, 37739 settled trades, 373 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 766 | 34.6 | 35.4 | $-546.35 | -7.1% | $453.65 | -1.5 | done | can't tell from luck |
| value_ev10 | 1845 | 38.6 | 39.2 | $-929.95 | -5.0% | $70.05 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3749 | 50.9 | 50.0 | $-950.98 | -2.5% | $49.02 | -1.5 | done | can't tell from luck |
| value_ev5 | 2784 | 40.6 | 41.1 | $-1339.07 | -4.8% | $-339.07 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 3145 | 51.1 | 51.0 | $-1433.77 | -4.6% | $-433.77 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 3145 | 48.9 | 49.2 | $-1716.16 | -5.5% | $-716.16 | -3.0 | done | losing for real |
| trend_filter | 2233 | 48.5 | 50.3 | $-1951.87 | -8.7% | $-951.87 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3749 | 49.1 | 50.2 | $-2345.14 | -6.3% | $-1345.14 | -3.9 | done | losing for real |
| coinflip | 5441 | 50.0 | 50.0 | $-2361.24 | -4.3% | $-1361.24 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5441 | 50.1 | 51.3 | $-3410.91 | -6.3% | $-2410.91 | -4.8 | done | losing for real |
| always_up | 5441 | 48.1 | 49.1 | $-3547.63 | -6.5% | $-2547.63 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9843 | 48.0 | 48.7 | $-5480.01 |
| ETH | 10586 | 48.1 | 47.9 | $-5468.85 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
