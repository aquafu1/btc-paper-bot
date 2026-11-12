# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 6:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 101 windows, 2574 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 192 | 58.9 | 52.9 | $+163.65 | +8.5% | $1163.65 | +1.2 | Wed 7:45 PM | too few trades (192/200) |
| reversal_15m_0.10pct | 248 | 56.5 | 52.1 | $+151.26 | +6.1% | $1151.26 | +1.0 | done | can't tell from luck |
| momentum_5m_0.00pct | 396 | 54.0 | 50.7 | $+105.86 | +2.7% | $1105.86 | +0.5 | done | can't tell from luck |
| value_ev20 | 50 | 28.0 | 36.5 | $-123.85 | -24.8% | $876.15 | -1.4 | Sun 4:15 AM | too few trades (50/200) |
| value_ev10 | 136 | 38.2 | 40.4 | $-133.13 | -9.8% | $866.87 | -1.0 | Thu 7:30 AM | too few trades (136/200) |
| trend_filter | 136 | 44.9 | 49.0 | $-158.60 | -11.7% | $841.40 | -1.3 | Thu 7:30 AM | too few trades (136/200) |
| coinflip | 396 | 51.0 | 51.4 | $-180.90 | -4.6% | $819.10 | -0.9 | done | can't tell from luck |
| value_ev5 | 184 | 36.4 | 41.8 | $-298.57 | -16.2% | $701.43 | -2.0 | Wed 9:00 PM | too few trades (184/200) |
| momentum_60m_0.30pct | 192 | 41.1 | 49.1 | $-362.82 | -18.9% | $637.18 | -2.6 | Wed 7:45 PM | too few trades (192/200) |
| always_up | 396 | 47.5 | 50.3 | $-366.80 | -9.3% | $633.20 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 248 | 43.5 | 49.9 | $-388.64 | -15.7% | $611.36 | -2.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 555 | 46.7 | 49.7 | $-377.68 |
| ETH | 630 | 46.3 | 48.9 | $-486.78 |
| SOL | 685 | 48.6 | 48.4 | $-435.69 |
| XRP | 704 | 50.3 | 49.0 | $-292.39 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
