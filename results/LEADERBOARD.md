# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 10:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 586 windows, 16218 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1380 | 51.2 | 49.6 | $-216.46 | -1.6% | $783.54 | -0.6 | done | can't tell from luck |
| value_ev20 | 317 | 33.1 | 35.3 | $-362.24 | -11.4% | $637.76 | -1.6 | done | can't tell from luck |
| trend_filter | 942 | 50.4 | 50.9 | $-502.62 | -5.3% | $497.38 | -1.7 | done | can't tell from luck |
| value_ev10 | 761 | 37.5 | 39.5 | $-733.78 | -9.6% | $266.22 | -2.2 | done | losing for real |
| value_ev5 | 1138 | 40.1 | 41.3 | $-842.37 | -7.4% | $157.63 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 1646 | 50.8 | 51.0 | $-844.33 | -5.1% | $155.67 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 1646 | 49.2 | 49.9 | $-931.62 | -5.7% | $68.38 | -2.3 | done | losing for real |
| coinflip | 2336 | 49.9 | 50.5 | $-1258.84 | -5.4% | $-258.84 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1380 | 48.8 | 51.3 | $-1357.34 | -9.8% | $-357.34 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2336 | 50.2 | 51.8 | $-1648.41 | -7.1% | $-648.41 | -3.6 | done | losing for real |
| always_up | 2336 | 47.3 | 49.9 | $-2216.46 | -9.5% | $-1216.46 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3682 | 47.7 | 49.2 | $-2738.01 |
| ETH | 4048 | 48.0 | 48.6 | $-2733.40 |
| SOL | 4213 | 47.9 | 48.8 | $-3107.64 |
| XRP | 4275 | 48.5 | 48.6 | $-2335.41 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
