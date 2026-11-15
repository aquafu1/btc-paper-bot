# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 4:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 466 windows, 12793 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 237 | 35.0 | 35.9 | $-136.40 | -5.8% | $863.60 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1082 | 50.8 | 49.9 | $-266.95 | -2.5% | $733.05 | -0.8 | done | can't tell from luck |
| value_ev10 | 605 | 39.0 | 40.1 | $-367.60 | -6.1% | $632.40 | -1.2 | done | can't tell from luck |
| trend_filter | 738 | 49.7 | 50.7 | $-432.44 | -5.9% | $567.56 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1290 | 49.9 | 50.0 | $-481.71 | -3.7% | $518.29 | -1.3 | done | can't tell from luck |
| value_ev5 | 895 | 41.0 | 41.8 | $-490.50 | -5.5% | $509.50 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1290 | 50.1 | 51.6 | $-930.61 | -7.2% | $69.39 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1082 | 49.2 | 51.8 | $-1012.08 | -9.4% | $-12.08 | -3.2 | done | losing for real |
| coinflip | 1858 | 49.9 | 50.8 | $-1021.88 | -5.5% | $-21.88 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 1858 | 49.8 | 51.6 | $-1294.59 | -7.0% | $-294.59 | -3.1 | done | losing for real |
| always_up | 1858 | 46.4 | 50.4 | $-2133.51 | -11.5% | $-1133.51 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2891 | 47.6 | 49.2 | $-2217.44 |
| ETH | 3212 | 48.1 | 48.8 | $-2052.96 |
| SOL | 3335 | 47.7 | 49.3 | $-2564.97 |
| XRP | 3355 | 48.6 | 49.1 | $-1732.91 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
