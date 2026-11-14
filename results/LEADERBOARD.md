# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 11:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 349 windows, 9372 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 184 | 37.5 | 36.6 | $-38.35 | -2.1% | $961.65 | -0.2 | Sat 7:00 PM | too few trades (184/200) |
| value_ev10 | 456 | 40.1 | 40.3 | $-189.48 | -4.2% | $810.52 | -0.7 | done | can't tell from luck |
| value_ev5 | 675 | 41.6 | 42.0 | $-320.46 | -4.7% | $679.54 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 928 | 52.0 | 52.0 | $-374.74 | -4.0% | $625.26 | -1.3 | done | can't tell from luck |
| reversal_60m_0.30pct | 761 | 51.4 | 52.1 | $-383.38 | -5.0% | $616.62 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 761 | 48.6 | 49.6 | $-473.45 | -6.2% | $526.55 | -1.7 | done | can't tell from luck |
| trend_filter | 515 | 47.2 | 50.2 | $-519.34 | -10.1% | $480.66 | -2.3 | done | losing for real |
| coinflip | 1388 | 50.3 | 50.8 | $-663.19 | -4.8% | $336.81 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 928 | 48.0 | 49.7 | $-689.25 | -7.4% | $310.75 | -2.3 | done | losing for real |
| momentum_5m_0.00pct | 1388 | 48.8 | 51.4 | $-1171.70 | -8.4% | $-171.70 | -3.2 | done | losing for real |
| always_up | 1388 | 46.5 | 50.6 | $-1617.60 | -11.7% | $-617.60 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2099 | 47.1 | 49.3 | $-1725.36 |
| ETH | 2361 | 47.5 | 48.7 | $-1718.89 |
| SOL | 2430 | 48.0 | 49.3 | $-1806.45 |
| XRP | 2482 | 48.8 | 49.1 | $-1190.26 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
