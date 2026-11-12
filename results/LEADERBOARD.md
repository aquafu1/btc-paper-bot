# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 6:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 100 windows, 2553 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 189 | 59.8 | 52.8 | $+193.65 | +10.2% | $1193.65 | +1.5 | Wed 8:15 PM | too few trades (189/200) |
| momentum_5m_0.00pct | 393 | 54.5 | 50.7 | $+135.86 | +3.5% | $1135.86 | +0.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 246 | 56.1 | 52.1 | $+128.82 | +5.2% | $1128.82 | +0.9 | done | can't tell from luck |
| value_ev20 | 50 | 28.0 | 36.5 | $-123.85 | -24.8% | $876.15 | -1.4 | Sun 4:15 AM | too few trades (50/200) |
| value_ev10 | 135 | 37.8 | 40.4 | $-145.89 | -10.8% | $854.11 | -1.1 | Thu 7:45 AM | too few trades (135/200) |
| trend_filter | 136 | 44.9 | 49.0 | $-158.60 | -11.7% | $841.40 | -1.3 | Thu 7:30 AM | too few trades (136/200) |
| coinflip | 393 | 50.9 | 51.4 | $-196.36 | -5.0% | $803.64 | -1.0 | done | can't tell from luck |
| value_ev5 | 183 | 36.1 | 41.8 | $-311.33 | -17.0% | $688.67 | -2.0 | Wed 9:15 PM | too few trades (183/200) |
| momentum_15m_0.10pct | 246 | 43.9 | 49.9 | $-368.64 | -15.0% | $631.36 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 189 | 40.2 | 49.1 | $-397.96 | -21.1% | $602.04 | -2.9 | Wed 8:15 PM | too few trades (189/200) |
| always_up | 393 | 47.1 | 50.4 | $-401.94 | -10.2% | $598.06 | -2.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 555 | 46.7 | 49.7 | $-377.68 |
| ETH | 623 | 46.4 | 48.8 | $-475.82 |
| SOL | 680 | 48.5 | 48.4 | $-453.80 |
| XRP | 695 | 50.1 | 49.0 | $-338.95 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
