# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 5:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 948 windows, 26275 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 485 | 35.3 | 34.8 | $-134.35 | -2.8% | $865.65 | -0.5 | done | can't tell from luck |
| value_ev10 | 1192 | 38.3 | 39.1 | $-608.60 | -5.1% | $391.40 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 2685 | 51.1 | 50.6 | $-820.82 | -3.1% | $179.18 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 2249 | 50.2 | 49.7 | $-843.50 | -3.8% | $156.50 | -1.8 | done | can't tell from luck |
| trend_filter | 1567 | 50.1 | 50.8 | $-979.16 | -6.2% | $20.84 | -2.5 | done | losing for real |
| value_ev5 | 1811 | 40.0 | 41.0 | $-992.38 | -5.5% | $7.62 | -2.0 | done | can't tell from luck |
| coinflip | 3784 | 50.3 | 50.4 | $-1628.63 | -4.3% | $-628.63 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2249 | 49.8 | 51.0 | $-1634.77 | -7.3% | $-634.77 | -3.5 | done | losing for real |
| momentum_15m_0.10pct | 2685 | 48.9 | 50.2 | $-1785.06 | -6.6% | $-785.06 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 3784 | 51.0 | 51.6 | $-1832.37 | -4.8% | $-832.37 | -3.1 | done | losing for real |
| always_up | 3784 | 46.9 | 49.6 | $-3706.78 | -9.8% | $-2706.78 | -6.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5993 | 48.2 | 49.0 | $-3342.28 |
| ETH | 6539 | 48.2 | 48.5 | $-3945.53 |
| SOL | 6846 | 48.3 | 48.6 | $-3750.41 |
| XRP | 6897 | 48.3 | 48.5 | $-3928.21 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
