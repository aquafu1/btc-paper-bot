# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 3:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 750 windows, 20701 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 392 | 33.7 | 34.9 | $-299.69 | -7.6% | $700.31 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 2117 | 51.5 | 50.5 | $-479.49 | -2.3% | $520.51 | -1.0 | done | can't tell from luck |
| value_ev10 | 949 | 37.8 | 39.1 | $-638.04 | -6.7% | $361.96 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1750 | 50.0 | 49.6 | $-655.37 | -3.7% | $344.63 | -1.6 | done | can't tell from luck |
| value_ev5 | 1430 | 40.2 | 41.1 | $-821.27 | -5.7% | $178.73 | -1.8 | done | can't tell from luck |
| trend_filter | 1220 | 49.8 | 50.9 | $-822.88 | -6.7% | $177.12 | -2.4 | done | losing for real |
| coinflip | 2992 | 50.4 | 50.2 | $-1137.55 | -3.8% | $-137.55 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1750 | 50.0 | 51.2 | $-1215.28 | -6.9% | $-215.28 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2117 | 48.5 | 50.2 | $-1559.06 | -7.4% | $-559.06 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 2992 | 50.7 | 51.8 | $-1724.32 | -5.8% | $-724.32 | -3.3 | done | losing for real |
| always_up | 2992 | 47.0 | 49.6 | $-2806.09 | -9.4% | $-1806.09 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4689 | 48.1 | 49.1 | $-2930.58 |
| ETH | 5158 | 48.0 | 48.5 | $-3357.29 |
| SOL | 5397 | 48.0 | 48.6 | $-3221.46 |
| XRP | 5457 | 48.5 | 48.5 | $-2649.72 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
