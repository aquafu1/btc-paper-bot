# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 6:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 570 windows, 15809 settled trades, 39 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1346 | 51.4 | 49.7 | $-198.03 | -1.5% | $801.97 | -0.5 | done | can't tell from luck |
| value_ev20 | 309 | 33.3 | 35.2 | $-327.95 | -10.6% | $672.05 | -1.4 | done | can't tell from luck |
| trend_filter | 918 | 50.8 | 51.1 | $-467.59 | -5.1% | $532.41 | -1.6 | done | can't tell from luck |
| value_ev10 | 746 | 37.5 | 39.4 | $-698.44 | -9.4% | $301.56 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 1606 | 50.9 | 51.0 | $-798.60 | -5.0% | $201.40 | -2.0 | done | losing for real |
| value_ev5 | 1110 | 39.7 | 41.3 | $-878.84 | -7.9% | $121.16 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1606 | 49.1 | 49.9 | $-927.50 | -5.8% | $72.50 | -2.3 | done | losing for real |
| coinflip | 2274 | 49.9 | 50.4 | $-1217.64 | -5.4% | $-217.64 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1346 | 48.6 | 51.2 | $-1357.79 | -10.1% | $-357.79 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2274 | 50.4 | 51.9 | $-1557.00 | -6.8% | $-557.00 | -3.4 | done | losing for real |
| always_up | 2274 | 47.1 | 49.9 | $-2259.62 | -9.9% | $-1259.62 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3570 | 47.7 | 49.2 | $-2725.59 |
| ETH | 3939 | 47.9 | 48.6 | $-2769.20 |
| SOL | 4126 | 47.8 | 48.7 | $-3047.83 |
| XRP | 4174 | 48.6 | 48.6 | $-2146.37 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
