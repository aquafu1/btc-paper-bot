# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 12:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 931 windows, 25747 settled trades, 34 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 475 | 35.2 | 34.8 | $-145.74 | -3.1% | $854.26 | -0.5 | done | can't tell from luck |
| value_ev10 | 1165 | 38.0 | 39.1 | $-672.90 | -5.8% | $327.10 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 2630 | 51.0 | 50.6 | $-886.21 | -3.4% | $113.79 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2196 | 50.0 | 49.8 | $-953.02 | -4.3% | $46.98 | -2.0 | done | losing for real |
| trend_filter | 1528 | 49.9 | 51.0 | $-1075.88 | -7.0% | $-75.88 | -2.8 | done | losing for real |
| value_ev5 | 1770 | 39.7 | 41.0 | $-1117.33 | -6.3% | $-117.33 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 2196 | 50.0 | 50.9 | $-1507.97 | -6.9% | $-507.97 | -3.3 | done | losing for real |
| coinflip | 3719 | 50.4 | 50.4 | $-1565.80 | -4.2% | $-565.80 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2630 | 49.0 | 50.2 | $-1677.33 | -6.4% | $-677.33 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 3719 | 50.9 | 51.6 | $-1918.11 | -5.2% | $-918.11 | -3.2 | done | losing for real |
| always_up | 3719 | 46.8 | 49.7 | $-3803.60 | -10.2% | $-2803.60 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5861 | 48.1 | 49.1 | $-3435.71 |
| ETH | 6405 | 48.2 | 48.6 | $-4033.34 |
| SOL | 6720 | 48.1 | 48.6 | $-3984.99 |
| XRP | 6761 | 48.3 | 48.5 | $-3869.84 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
