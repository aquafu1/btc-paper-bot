# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 10:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 585 windows, 16189 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1376 | 51.3 | 49.6 | $-196.23 | -1.4% | $803.77 | -0.5 | done | can't tell from luck |
| value_ev20 | 317 | 33.1 | 35.3 | $-362.24 | -11.4% | $637.76 | -1.6 | done | can't tell from luck |
| trend_filter | 938 | 50.5 | 50.9 | $-482.40 | -5.1% | $517.60 | -1.6 | done | can't tell from luck |
| value_ev10 | 761 | 37.5 | 39.5 | $-733.78 | -9.6% | $266.22 | -2.2 | done | losing for real |
| value_ev5 | 1137 | 40.1 | 41.3 | $-832.37 | -7.3% | $167.63 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 1644 | 50.8 | 51.0 | $-839.56 | -5.1% | $160.44 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 1644 | 49.2 | 49.9 | $-931.40 | -5.7% | $68.60 | -2.3 | done | losing for real |
| coinflip | 2332 | 49.9 | 50.5 | $-1237.78 | -5.3% | $-237.78 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1376 | 48.7 | 51.3 | $-1369.11 | -9.9% | $-369.11 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2332 | 50.2 | 51.8 | $-1628.19 | -7.0% | $-628.19 | -3.5 | done | losing for real |
| always_up | 2332 | 47.3 | 49.9 | $-2196.24 | -9.4% | $-1196.24 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3676 | 47.8 | 49.2 | $-2695.61 |
| ETH | 4041 | 48.0 | 48.6 | $-2701.27 |
| SOL | 4205 | 47.8 | 48.8 | $-3126.51 |
| XRP | 4267 | 48.5 | 48.6 | $-2285.87 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
