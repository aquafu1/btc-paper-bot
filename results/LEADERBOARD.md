# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 2:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 267 windows, 6982 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 688 | 55.2 | 52.3 | $+115.71 | +1.7% | $1115.71 | +0.5 | done | can't tell from luck |
| reversal_60m_0.30pct | 557 | 53.1 | 52.2 | $-134.45 | -2.4% | $865.55 | -0.6 | done | can't tell from luck |
| value_ev20 | 122 | 32.8 | 36.7 | $-171.51 | -14.1% | $828.49 | -1.2 | Sun 12:30 PM | too few trades (122/200) |
| value_ev10 | 333 | 36.6 | 40.7 | $-443.49 | -13.3% | $556.51 | -2.1 | done | losing for real |
| trend_filter | 363 | 45.7 | 50.2 | $-490.09 | -13.5% | $509.91 | -2.6 | done | losing for real |
| value_ev5 | 491 | 39.1 | 42.4 | $-574.40 | -11.7% | $425.60 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 557 | 46.9 | 49.7 | $-593.55 | -10.7% | $406.45 | -2.6 | done | losing for real |
| coinflip | 1061 | 49.3 | 50.9 | $-790.26 | -7.4% | $209.74 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 1061 | 49.7 | 51.5 | $-813.49 | -7.7% | $186.51 | -2.6 | done | losing for real |
| always_up | 1061 | 47.8 | 50.1 | $-958.58 | -9.0% | $41.42 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 688 | 44.8 | 49.7 | $-959.22 | -13.9% | $40.78 | -3.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1554 | 46.5 | 49.6 | $-1633.48 |
| ETH | 1748 | 46.7 | 49.0 | $-1760.36 |
| SOL | 1806 | 48.2 | 49.2 | $-1383.73 |
| XRP | 1874 | 48.8 | 49.2 | $-1035.76 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
