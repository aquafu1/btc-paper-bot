# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 5:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 372 windows, 10092 settled trades, 66 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 193 | 37.8 | 36.6 | $+3.05 | +0.2% | $1003.05 | +0.0 | Sat 8:45 PM | too few trades (193/200) |
| value_ev10 | 492 | 40.7 | 40.5 | $-129.12 | -2.6% | $870.88 | -0.5 | done | can't tell from luck |
| value_ev5 | 724 | 42.0 | 42.1 | $-268.98 | -3.7% | $731.02 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 836 | 49.9 | 49.8 | $-346.74 | -4.1% | $653.26 | -1.2 | done | can't tell from luck |
| trend_filter | 558 | 49.3 | 50.6 | $-380.47 | -6.8% | $619.53 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1005 | 51.5 | 52.1 | $-505.60 | -5.0% | $494.40 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 1005 | 48.5 | 49.7 | $-601.50 | -6.0% | $398.50 | -1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 836 | 50.1 | 52.0 | $-629.09 | -7.5% | $370.91 | -2.3 | done | losing for real |
| coinflip | 1481 | 49.8 | 50.8 | $-840.88 | -5.7% | $159.12 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1481 | 49.8 | 51.6 | $-1030.16 | -7.0% | $-30.16 | -2.8 | done | losing for real |
| always_up | 1481 | 45.6 | 50.7 | $-2022.52 | -13.7% | $-1022.52 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2269 | 47.3 | 49.4 | $-1808.58 |
| ETH | 2544 | 47.7 | 48.9 | $-1754.16 |
| SOL | 2612 | 48.0 | 49.5 | $-1882.36 |
| XRP | 2667 | 48.8 | 49.1 | $-1306.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
